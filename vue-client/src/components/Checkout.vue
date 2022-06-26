<template>
    <Header />
    <div class="content">
        <div class="home containers">
            <form @submit.prevent="createOrder()" class="description-form">
                <div class="des__container">
                    <div class="zip-to">
                        <div class="des__body">
                        <h1>FROM</h1>
                            <div class="form-group">
                                <div class="col-sm-10">
                                    <i class="des-icon bi bi-person-fill"></i>
                                    <input v-model="this.info.from_first_name" name="from_first_name" type="text" class="form-control mg-10" id="name" placeholder="First Name" required>
                                    <input v-model="this.info.from_last_name" name="from_last_name" type="text" class="form-control" id="pwd" placeholder="Last Name" required>
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="col-sm-10">
                                    <i class="des-icon bi bi-telephone-fill"></i>
                                    <input v-model="this.info.from_phone" name="from_phone" type="number" class="form-control"  min="0"  id="pwd" placeholder="Phone" required>
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="col-sm-10">
                                    <i class="des-icon des-icon-pd-10 bi bi-building"></i>
                                    <input v-model="this.info.from_company" name="from_company" type="text" class="form-control" id="pwd" placeholder="Company">
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="col-sm-10">
                                    <i class="des-icon des-icon-pd-10 bi bi-geo-alt-fill"></i>
                                    <input v-model="this.info.from_street" name="from_street" type="text" class="form-control" id="pwd" placeholder="Street" required>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="zip-from">
                        <div class="des__body">
                            <h1>TO</h1>
                            <div class="form-group">
                                <div class="col-sm-10">
                                    <i class="des-icon bi bi-person-fill"></i>
                                    <input v-model="this.info.to_first_name" name="to_first_name" type="text" class="form-control mg-10" id="name" placeholder="First Name" required>
                                    <input v-model="this.info.to_last_name" name="to_last_name" type="text" class="form-control" id="pwd" placeholder="Last Name" required>
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="col-sm-10">
                                    <i class="des-icon bi bi-telephone-fill"></i>
                                    <input v-model="this.info.to_phone" name="to_phone" type="number" class="form-control"  min="0" id="pwd" placeholder="Phone" required>
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="col-sm-10">
                                    <i class="des-icon des-icon-pd-10 bi bi-building"></i>
                                    <input v-model="this.info.to_company" name="to_company" type="text" class="form-control" id="pwd" placeholder="Company">
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="col-sm-10">
                                    <i class="des-icon des-icon-pd-10 bi bi-geo-alt-fill"></i>
                                    <input v-model="this.info.to_street" name="to_street" type="text" class="form-control" id="pwd" placeholder="Street" required>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="services">
                        <div class="des__body">
                            <div class="services__des">
                                <h3>Loại dịch vụ</h3>
                                <p>{{this.carrier}}, {{this.service}} - TOTAL {{this.rate}}$</p>
                            </div>
                            <div class="amount">
                                <p>Số sản phẩm: {{this.lenParcel}}</p> 
                            </div>
                            <div v-if="this.lenParcel > 0" class="des__product">
                                <div v-for="index in this.lenParcel" :key="index"  class="product pd_0">
                                    <span>Parcel {{index}}: </span>
                                    <span>({{this.shipment.parcel[index-1].length}}x{{this.shipment.parcel[index-1].width}}x{{this.shipment.parcel[index-1].height}}x{{this.shipment.parcel[index-1].weight}})</span>
                                </div>
                            </div>
                            <div class="submit">
                                <button type="submit" class="btn__submit">
                                    <span v-if="loading" class="spinner-border"> </span>
                                    Submit
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                
            </form>
        </div>
    </div>
    <notifications position="top" width="100%" height="80px" group="foo" closeOnClick="true" type="success" />
    <Footer />
</template>

<script>
    import Header from './Header.vue'
    import Footer from './Footer.vue'
    import BaseRequest from '../core/BaseRequest.js'
    export default {
        components: {
            Header,
            Footer
        },
        data() {
            return {
                shipment: {

                },
                new_shipment: {

                },
                info: {
                    from_first_name: "",
                    from_last_name: "",
                    from_phone: "",
                    from_company: "",
                    from_street: "",

                    to_first_name: "",
                    to_last_name: "",
                    to_phone: "",
                    to_company: "",
                    to_street: "",
                },
                lenParcel: 0,
                loading: false,
                errors: {

                }
            }
        },
        mounted() {
            this.checkLoggedIn();
            this.checkValidateEmail();
            this.getShipment()
        },
        props: {
            idShipment: {
                type: String,
                required: true
            },
            carrier: {
                type: String,
                required: true
            },
            service: {
                type: String,
                required: true
            },
            rate: {
                type: String,
                required: true
            },
        },
        methods: {
            checkLoggedIn: function() {
                let user = window.localStorage.getItem('user');
                BaseRequest.get('user/' + user)
                .then(function(response) {
                    console.log(response.data);
                })
                .catch(() => {
                    this.$router.push({name: 'Login'})
                })
            },
            checkValidateEmail: function() {
                let user = window.localStorage.getItem('user');
                BaseRequest.get('customer/' + user)
                .then((response) => {
                    let verification_code = response.data.verification_code
                    if (verification_code != "") {
                        console.log("loi chua xac nhan email");
                        this.$router.push({name: 'ValidateCustomer'})
                        console.log(verification_code);
                    }
                    
                })
                .catch(() => {
                    this.$router.push({name: 'Login'})
                })
            },
            getShipment: function() {
                console.log("ok")
                BaseRequest.get('shipment/' + this.idShipment)
                .then((response) => {
                    this.shipment = response.data
                    console.log(this.shipment)
                    this.lenParcel = this.shipment.parcel.length;
                })
                .catch((error) => {
                    this.errors = error.response.data
                })
            },
            createOrder: function() {
                this.loading = true
                let shipment = {
                    "from_name": this.info.from_first_name + this.info.from_last_name,
                    "from_phone": this.info.from_phone,
                    "from_street1": this.info.from_street,
                    "from_state": this.shipment.from_state,
                    "from_city": this.shipment.from_city,
                    "from_zip": this.shipment.from_zip,
                    "from_country": "US",
                    // "from_company": this.info.from_company,
                    "to_name": this.info.to_first_name + this.info.to_last_name,
                    "to_phone": this.info.to_phone,
                    "to_street1": this.info.to_street,
                    "to_state": this.shipment.to_state,
                    "to_city": this.shipment.to_city,
                    "to_zip": this.shipment.to_zip,
                    "to_country": "US",
                    // "to_company": this.info.to_company,
                    "user": window.localStorage.getItem('id'),
                    "parcel": this.shipment.parcel,
                    "carrier": this.carrier,
                    "service": this.service,
                    "rate": this.rate
                }

                if (this.info.from_company == '') {
                    shipment["from_company"] = this.info.from_first_name + this.info.from_last_name
                }
                else {
                    shipment["from_company"] = this.info.from_company
                }
                if (this.info.to_company == '') {
                    shipment["to_company"] = this.info.to_first_name + this.info.to_last_name
                }
                else {
                    shipment["to_company"] = this.info.to_company
                }

                console.log(shipment)
                BaseRequest.post('createorder/', shipment)
                .then(response => {
                    console.log(response.data)
                    window.localStorage.removeItem('id_oneshipment')
                    window.localStorage.removeItem('id_manyshipment')
                    window.localStorage.removeItem('checkBuy')
                    window.localStorage.removeItem('check')
                    this.loading = false
                    this.$notify({
                        group: 'foo',
                        title: 'Order success!',
                        text: 'Hello user! You have successfully your order!'
                    })
                    setTimeout( () => this.$router.push({ name: 'Home'}), 5000);

                })
                .catch(error=> {
                    this.errors = error.response
                    console.log("loi");
                    console.log(this.errors);
                    this.loading = false
            });
            }
        }
    }
</script>

<style scoped>
    @import '../assets/css/description.css';
</style>