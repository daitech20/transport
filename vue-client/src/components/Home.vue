<template>
    <div class="sticky-footer">
      <Header />
      <!-- <div class="content">
          <div class="home">
              <div class="home__banner">
                  <div class="containers">
                      <div class="home__banner-content">
                          <h1>Compare and book <br><strong>parcel delivery services</strong></h1>
                          <a href="#" data-show-modal="video_popup" class="home__banner-btn">
                              <span class="img-icon--play">
                                  <i class="icon__play fa-solid fa-circle-play"></i>
                              </span>Watch our video
                          </a>
                          <div class="home__banner--trustpilot">
                              <img src="../assets/img/home__banner.png" alt="Trustpilot rating">
                          </div>
                      </div>
                      <div id="get-qoute" class="get-qoute">
                          <input type="radio" name="get-quote-type" id="get-quote-default" autocomplete="off" checked="">
                          <input type="radio" name="get-quote-type" id="get-quote-local" autocomplete="off">
                          <div class="get-quote__tabs">
                              <label for="get-quote-default" class="get-quote__tab uk-quote" @click="oneShipment">UK to UK</label>
                              <label for="get-quote-local" class="get-quote__tab international-quote" @click="manyShipment">International</label>
                          </div>
                          <div class="get-qoute__form one__shipment">
                              <form class="form" @submit.prevent="createShipment()">
                                  <div class="form-field">
                                      <div class="form-field-inner">
                                          <p class="form-field-title">Zip To</p>
                                          <input v-model="address.from_zip" class="form-field-input" type="text" placeholder="..." :class="{'is-invalid': errors.from_error }" name="from_zip" required>        
                                          <div v-if="errors.from_error" class="invalid-feedback"><p class="form-field-title">Zip wrong!</p></div>
                                      </div>
                                  </div>
                                  <div class="form-field">
                                      <div class="form-field-inner">
                                          <p class="form-field-title">Zip From</p>
                                          <input v-model="address.to_zip" class="form-field-input" type="text" placeholder="..." :class="{'is-invalid': errors.from_error }" name="to_zip" required>        
                                          <div v-if="errors.to_error" class="invalid-feedback"><p class="form-field-title">Zip wrong!</p></div>
                                      </div>
                                  </div>
                                  <div class="form-field">
                                      <div class="form-field-inner">
                                          <p class="form-field-title">Parcel weight</p>
                                          <input v-model="parcel.weight" name="weight" class="form-field-input" step="0.01" max="500" min="0.1" type="number" id="lbs" placeholder="Eg.1" required>
                                          <label class="size_16em" for="lbs">(lbs)</label>
                                      </div>
                                  </div>
                                  <div class="form-field form-field--radio">
                                      <div class="form-field--inner">
                                          <div class="form-field--radio-wrapper">
                                              <p>I will fill in dimensions:</p>
                                              <div class="form-select">
                                                  <div class="choice-radio">
                                                      <input type="radio" id="uk-no_dimensions" class="space-0-mobile" name="dimensions" value="no-dimensions" checked="checked" @click="hideSpaceMobile">
                                                      <label style="font-size:1.2rem" for="uk-no_dimensions">later</label>
                                                  </div>
                                                  <div class="choice-radio">
                                                      <input type="radio" id="uk-with_dimensions" name="dimensions" value="add-dimensions" @click="showSpaceMobile">
                                                      <label style="font-size:1.2rem" for="uk-with_dimensions">now</label>
                                                  </div>
                                              </div>
                                          </div>
                                      </div>
                                  </div>
                                  <div id="dimensions_uk" class="dimensions">
                                      <div class="dimensions__inner">    
                                          <div class="form-field">
                                              <div class="form-field--inner">
                                                  <label for="length-uk">Length: </label>
                                                  <input v-model="parcel.length" name="length" id="length-uk" type="number" step="0.01" max="500" min="1"  placeholder="Eg. 1">
                                                  <span>cm</span>
                                              </div>
                                          </div>
                                          <div class="form-field">
                                              <div class="form-field--inner">
                                                  <label for="width-uk">Width: </label>
                                                  <input v-model="parcel.width" name="width" id="width-uk" type="number" step="0.01" max="500" min="1"  placeholder="Eg. 1">
                                                  <span>cm</span>
                                              </div>
                                          </div>
                                          <div class="form-field">
                                              <div class="form-field--inner">
                                                  <label for="height-uk">Height: </label>
                                                  <input v-model="parcel.height" name="height" id="height-uk" type="number" step="0.01" max="500" min="1" placeholder="Eg. 1">
                                                  <span>cm</span>
                                              </div>
                                          </div>
                                      </div>
                                  </div>
                                  <button type="submit" class="btn__oneshipment" @click="getRate">
                                      Get Quote
                                  </button>
                              </form>
                              <div class="get-quote__prices">
                                <div class="table-responsive-sm">
                                    <table v-if="priceShipment.servicecarrier != null && this.check == true" class="table">
                                        <thead>
                                            <tr>
                                                <th class="price-title">Carrier</th>
                                                <th class="price-title">Service</th>
                                                <th class="price-title">Price</th>
                                                <th class="price-title">Action</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="sv in priceShipment.servicecarrier" :key="sv.id">
                                                <td>{{ sv.carrier }}</td>
                                                <td>{{ sv.service }}</td>
                                                <td>{{ sv.rate }}</td>
                                                <td>
                                                  <router-link :to="{ name: 'Checkout', params: { id: sv.id }}" replace>
                                                    <button class="btn btn-success" >Select</button>
                                                  </router-link>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                              </div>
                          </div>
                          <div class="get-qoute__form many__shipment ">
                            
                              <form class="form" @submit.prevent="createShipment()">
                                  <div class="form-field_many">          
                                      <div class=" size-img">
                                        <h3>Download</h3>
                                        <a :href="`${publicPath}example.xlsx`" :src="`${publicPath}example.xlsx`" download>
                                          <img class="form-field-img" src="../assets/img/Excel-Logo.jpg" alt=""> 
                                        </a>
                                      </div>
                                  </div>
                                  <div class="form-field_many">
                                      <div class="form-field-outline">
                                              <input type="file" id="myFile" name="filename" @change="selectFile" accept=".xlsx, .xls, .csv" >
                                      </div>
                                  </div>
                                  <div class="form-field_many btn-mobile">
                                      <button type="submit" class="btn__manyship">Get Quote</button>
                                  </div>
                                  
                              </form>
                              <div class="get-quote__prices">
                                <div class="table-responsive-sm">
                                    <table v-if="priceManyShipment.servicecarrier != null && this.check == false" class="table">
                                        <thead>
                                            <tr>
                                                <th class="price-title">Carrier</th>
                                                <th class="price-title">Service</th>
                                                <th class="price-title">Price</th>
                                                <th class="price-title">Action</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="sv in priceManyShipment.servicecarrier" :key="sv.id">
                                                <td>{{ sv.carrier }}</td>
                                                <td>{{ sv.service }}</td>
                                                <td>{{ sv.rate }}</td>
                                                <td>
                                                    <router-link :to="{ name: 'Checkout', params: { id: sv.id }}" replace>
                                                    <button class="btn btn-success" >Select</button>
                                                    </router-link>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                          </div>
                      </div>
                  </div>
          
              </div>
          </div>
      </div> -->
      <div class="content">
        <div class="home">
            <div class="home__banner">
                <div class="containers">
                    <div class="home__banner-content">
                        <h1 class="mb-480 mb-320">Compare and book <br><strong>parcel delivery services</strong></h1>
                        <a href="#" data-show-modal="video_popup" class="home__banner-btn">
                            <span class="img-icon--play">
                                <i class="icon__play fa-solid fa-circle-play"></i>
                            </span>Watch our video
                        </a>
                        <div class="home__banner--trustpilot">
                            <img src="../assets/img/home__banner.png" alt="Trustpilot rating">
                        </div>
                    </div>
                    <div id="get-qoute" class="get-qoute">
                        <input type="radio" name="get-quote-type" id="get-quote-default" autocomplete="off" checked="">
                        <input type="radio" name="get-quote-type" id="get-quote-local" autocomplete="off">
                        <div class="get-quote__tabs">
                            <label for="get-quote-default" class="get-quote__tab uk-quote" @click="oneShipment">UK to UK</label>
                            <label for="get-quote-local" class="get-quote__tab international-quote"  @click="manyShipment" >International</label>
                        </div>
                        <div class="get-qoute__form one__shipment">
                            <form class="form" @submit.prevent="createShipment()">
                                <div class="form-field">
                                    <div class="form-field-inner">
                                        <p class="form-field-title">Zip From</p>
                                        <input v-model="address.from_zip" class="form-control form-field-input" type="text" placeholder="..." :class="{'is-invalid': errors.from_error && checkBuy==true}" name="from_zip" required>        
										<div v-if="errors.from_error && checkBuy==true" class="invalid-feedback"><p class="form-field-title">Zip wrong!</p></div>
									</div>
                                </div>
                                <div class="form-field">
                                    <div class="form-field-inner">
                                        <p class="form-field-title">Zip To</p>
                                        <input v-model="address.to_zip" class="form-control form-field-input" type="text" placeholder="..." :class="{'is-invalid': errors.to_error && checkBuy==true}" name="to_zip" required>        
                                        <div v-if="errors.to_error && checkBuy==true" class="invalid-feedback"><p class="form-field-title">Zip wrong!</p></div>

                                    </div>
                                </div>
                                <div class="form-field">
                                    <div class="form-field-inner">
                                        <p class="form-field-title">Parcel weight</p>
                                        <input v-model="parcel.weight" name="weight" class="form-control form-field-input" step="0.01" max="500" min="0.1" type="number" id="lbs" placeholder="Eg.1" required>
                                          <label class="size_16em" for="lbs">(lbs)</label>
                                    </div>
                                </div>
                                <div class="form-field form-field--radio">
                                    <div class="form-field--inner">
                                        <div class="form-field--radio-wrapper">
                                            <p>I will fill in dimensions:</p>
                                            <div class="form-select">
                                                <div class="choice-radio">
                                                    <input type="radio" id="uk-no_dimensions" class="space-0-mobile" name="dimensions" value="no-dimensions" checked="checked" @click="hideSpaceMobile">
                                                    <label for="uk-no_dimensions">later</label>
                                                </div>
                                                <div class="choice-radio">
                                                    <input type="radio" id="uk-with_dimensions" name="dimensions" value="add-dimensions" @click="showSpaceMobile">
                                                    <label for="uk-with_dimensions">now</label>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div id="dimensions_uk" class="dimensions">
                                    <div class="dimensions__inner">    
                                        <div class="form-field">
                                            <div class="form-field--inner">
                                                <label for="length-uk">Length: </label>
                                                <input v-model="parcel.length" name="length" class="form-control form-field-input" id="length-uk" type="number" step="0.01" max="500" min="1"  placeholder="Eg. 1">
                                                <span>cm</span>
                                            </div>
                                        </div>
                                        <div class="form-field">
                                            <div class="form-field--inner">
                                                <label for="width-uk">Width: </label>
                                                <input v-model="parcel.width" name="width" class="form-control form-field-input" id="width-uk" type="number" step="0.01" max="500" min="1"  placeholder="Eg. 1">
                                                <span>cm</span>
                                            </div>
                                        </div>
                                        <div class="form-field">
                                            <div class="form-field--inner">
                                                <label for="height-uk">Height: </label>
                                                <input v-model="parcel.height" name="height" class="form-control form-field-input" id="height-uk" type="number" step="0.01" max="500" min="1" placeholder="Eg. 1">
                                                <span>cm</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <button type="submit" class="btn__oneshipment">
                                    <span v-if="loading" class="spinner-border"></span>Get Quote
                                </button>
                            </form>
							<div class="get-quote__prices">
                                <div class="table-responsive-sm">
                                    <table v-if="priceShipment.servicecarrier != null && this.check == true" class="table">
                                        <thead>
                                            <tr>
                                                <th class="price-title">Carrier</th>
                                                <th class="price-title">Service</th>
                                                <th class="price-title">Price</th>
                                                <th class="price-title">Action</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="sv in priceShipment.servicecarrier" :key="sv.id">
                                                <td>{{ sv.carrier }}</td>
                                                <td>{{ sv.service }}</td>
                                                <td>{{ sv.rate }}</td>
                                                <td>
                                                  <button class="btn btn-success" @click="checkValidateEmail(priceShipment.shipment, sv.carrier, sv.service, sv.rate)">Select</button>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                        <div class="get-qoute__form many__shipment ">
                            <form class="form" @submit.prevent="createShipment()">
                                  <div class="form-field_many">          
                                      <div class=" size-img">
                                        <h3>Download</h3>
                                        <a :href="`${publicPath}example.xlsx`" :src="`${publicPath}example.xlsx`" download>
                                          <img class="form-field-img" src="../assets/img/Excel-Logo.jpg" alt=""> 
                                        </a>
                                      </div>
                                  </div>
                                  <div class="form-field_many">
                                      <div class="form-field-outline">
                                              <input type="file" id="myFile" name="filename" @change="selectFile" accept=".xlsx, .xls, .csv" ref="inputFile">
                                      </div>
                                  </div>
                                  <div class="form-field_many btn-mobile">
                                      <button type="submit" class="btn__manyship">
                                        <span v-if="loading" class="spinner-border"> </span>Get Quote
                                      </button>
                                  </div>                             
                            </form>
                              <div class="get-quote__prices">
                                <div class="table-responsive-sm">
                                    <table v-if="priceManyShipment.servicecarrier != null && this.check == false" class="table">
                                        <thead>
                                            <tr>
                                                <th class="price-title">Carrier</th>
                                                <th class="price-title">Service</th>
                                                <th class="price-title">Price</th>
                                                <th class="price-title">Action</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="sv in priceManyShipment.servicecarrier" :key="sv.id">
                                                <td>{{ sv.carrier }}</td>
                                                <td>{{ sv.service }}</td>
                                                <td>{{ sv.rate }}</td>
                                                <td>                        
                                                    <button class="btn btn-success" @click="checkValidateEmail(priceManyShipment.shipment, sv.carrier, sv.service, sv.rate)">Select</button>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>              
                </div>
        
            </div>
        </div>
    </div>
    <Footer />
      <!-- <div class="modal__notification">
        <div class="modal__content">
            <header class="header__notification">
                <span @click="this.hideNotification" class="header__icon-close">
                    <i class="icon__close-notif bi bi-x-lg"></i>
                </span>
            </header>
            <div class="body__notification">
                <h3>Please vetify email to select!!!</h3>
                <h3 style="text-align:center">Click <a href="">this</a> to vetify!</h3>
            </div>
        </div>
    </div> -->
    <!-- <notifications /> -->
    <Notification v-model:check_ValidateEmail="check_ValidateEmail" v-model:checkNotify="checkNotify" v-model:checkLogin="checkLogin" />
    {{this.checkNotify}}
</div>

</template>

<script >
import 'bootstrap-icons/font/bootstrap-icons.css'
import Header from './Header.vue'
import Footer from './Footer.vue'
import Notification from './Notification.vue'
import readXlsxFile from 'read-excel-file'
import BaseRequest from '../core/BaseRequest.js'
import {saveAs} from 'file-saver';
const axios = require('axios');
export default {
  components: {
    Header,
    Footer,
    Notification
  },
  data() {
    return {
      publicPath: process.env.BASE_URL,
      customer: {

      },
      address: {
        from_street1: "",
        from_zip: "",
        from_zip_many: "",
        from_state: "",
        from_city: "",
        from_country: "",

        to_street1: "",
        to_zip: "",
        to_zip_many: "",
        to_state: "",
        to_city: "",
        to_country: "",
      },
      parcel: {
        length: 1,
        height: 1,
        width: 1,
        weight: ""
      },
      parcel_excel: [

      ],
      priceShipment: {

      },
      priceManyShipment: {

      },
      file: "",
      content: "",
      rows: "",
      check: true,
      checkBuy: true,
      checkLogin: false,
      check_ValidateEmail: true,
      checkNotify: false,
      loading: false,
      errors: {

      }
    }
  },
  created() {
    window.addEventListener('beforeunload', function(event) {
         window.localStorage.removeItem('id_shipment')
         window.localStorage.removeItem('id_oneshipment')
         window.localStorage.removeItem('id_manyshipment')
         window.localStorage.removeItem('checkBuy')
         window.localStorage.removeItem('check')
    })
    if (window.localStorage.getItem('checkBuy') != null) {
        let temp = window.localStorage.getItem('checkBuy')
        if (temp == 'true') {
            this.checkBuy = true
        }
        else {
            this.checkBuy = false
        }
    }
    
    if (window.localStorage.getItem('id_oneshipment') != null) {
    BaseRequest.get('shipment/' + window.localStorage.getItem('id_oneshipment'))
    .then(response => {
        this.address.from_street1 = response.data.from_street1
        this.address.to_street1 = response.data.to_street1
        this.address.from_zip = response.data.from_zip
        this.address.to_zip = response.data.to_zip
        this.parcel.length = response.data.parcel[0].length
        this.parcel.height = response.data.parcel[0].height
        this.parcel.width = response.data.parcel[0].width
        this.parcel.weight = response.data.parcel[0].weight

        BaseRequest.get('checkpriceshipment/' + window.localStorage.getItem('id_oneshipment'))
        .then(response => {
            this.priceShipment = response.data
        })
        .catch(error=> {
        this.errors = error.response.data
        console.log(this.errors);
            });
        })
    .catch(error=> {
        this.errors = error.response.data
        console.log("loi");
        console.log(this.errors);
        });
    }

    if (window.localStorage.getItem('id_manyshipment') != null) {
    BaseRequest.get('shipment/' + window.localStorage.getItem('id_manyshipment'))
    .then(response => {
        BaseRequest.get('checkpriceshipment/' + window.localStorage.getItem('id_manyshipment'))
        .then(response => {
            this.priceManyShipment = response.data
        })
        .catch(error=> {
        this.errors = error.response.data
        console.log(this.errors);
            });
        })
    .catch(error=> {
        this.errors = error.response.data
        console.log("loi");
        console.log(this.errors);
        });
    }
  },
  mounted() {
    this.checkLoggedIn()
    if (window.localStorage.getItem('check') != null) {
        let temp = window.localStorage.getItem('checkBuy')
        if (temp == 'true') {
            this.check = true
            this.oneShipment()
        }
        else {
            this.check = false
            this.manyShipment()
        }
    }
  },
  methods: {
    checkLoggedIn: function() {
        let user = window.localStorage.getItem('user');
        BaseRequest.get('user/' + user)
        .then(response => {
            console.log(response.data);
            this.checkLogin = true
        })
        .catch(error=> {
            this.errors = error.response.data
            console.log("loi chua dang nhap");
            console.log(this.errors);
            this.checkLogin = false
        });
    },
    selectFile: function(event) {
        this.parcel_excel = []
        let xlsxfile = event.target.files ? event.target.files[0] : null;
        readXlsxFile(xlsxfile).then((rows) => {
          this.rows = {}
          this.rows = rows
          console.log(this.rows)
          for (let row in rows) {
            if (row == 1) {
              this.address.from_zip_many = this.rows[row][1]
              this.address.to_zip_many = this.rows[row][2]
            }
            if (row > 3) {
              this.parcel_excel.push({
                length: this.rows[row][0],
                height: this.rows[row][1],
                width: this.rows[row][2],
                weight: this.rows[row][3]
              })
              console.log('ok')
            }
          }
        console.log(this.parcel_excel)
    })
    },
    checkValidateEmail(idShipment, carrier, service, rate) {
        let user = window.localStorage.getItem('user');
        BaseRequest.get('customer/' + user)
        .then(response => {
            this.customer = response.data
            if (this.customer.verification_code == "") {
                this.check_ValidateEmail = true
                this.$router.push({ name: 'Checkout', params: {idShipment: idShipment, carrier: carrier, service: service, rate: rate } })
            }
            else {
                this.check_ValidateEmail = false
                this.checkNotify = true
            }
        })
    },
    createShipment: function() {
        this.loading = true
        if (this.checkLogin == true) {
            console.log("loading", this.loading)
            this.errors = {}
            let shipment = {
                "from_name": "Tan Pham",
                "from_phone": "123456789",
                "from_street1": "abc",
                "from_state": "abc",
                "from_city": "abc",
                "from_country": "US",
                "to_name": "Tan Pham",
                "to_phone": "123456789",
                "to_street1": "abc",
                "to_state": "abc",
                "to_city": "abc",
                "to_country": "US",
                "user": window.localStorage.getItem('id'),
                "parcel": []
                // "parcel": [
                //     {
                //         "height": this.parcel.height,
                //         "length": this.parcel.length,
                //         "width": this.parcel.width,
                //         "weight": this.parcel.weight
                //     }
                // ]
            }

        if (this.check) {
            shipment["from_zip"] = this.address.from_zip
            shipment["to_zip"] = this.address.to_zip

            shipment.parcel.push({
            "height": this.parcel.height,
            "length": this.parcel.length,
            "width": this.parcel.width,
            "weight": this.parcel.weight
            })
            this.checkBuy = true
            this.priceShipment = {}
            window.localStorage.setItem('checkBuy', true)
        }
        else {
            shipment["from_zip"] = this.address.from_zip_many
            shipment["to_zip"] = this.address.to_zip_many

            shipment.parcel =this.parcel_excel
            this.checkBuy = false
            this.priceManyShipment = {}
            this.$refs.inputFile.value = null
            window.localStorage.setItem('checkBuy', false)
        }

        console.log(shipment)
        BaseRequest.post('shipment/', shipment)
            .then(response => {
                console.log(response.data);
                if (this.checkBuy == true) {
                    window.localStorage.setItem('id_oneshipment', response.data.id)
                    BaseRequest.get('checkpriceshipment/' + window.localStorage.getItem('id_oneshipment'))
                    .then(response => {
                    this.priceShipment = response.data
                    console.log(this.priceShipment)
                    })
                }
                else {
                    window.localStorage.setItem('id_manyshipment', response.data.id)
                    BaseRequest.get('checkpriceshipment/' + window.localStorage.getItem('id_manyshipment'))
                    .then(response => {
                    this.priceManyShipment = response.data
                    console.log(this.priceManyShipment)
                    })
                }
                this.errors = {}
                this.loading = false
            })
            .catch(error=> {
                this.errors = error.response.data
                console.log("loi");
                console.log(this.errors);
                this.loading = false
            });
        }
        else {
            this.checkNotify = true
            this.loading = false
        }
    },
    showSpaceMobile: function() {
      const dimensions = document.querySelector('.dimensions__inner')
      const price_table = document.querySelector('.get-quote__prices')
      var margin__120__mobile = document.querySelector(".btn__oneshipment");
      margin__120__mobile.classList.add("space-150-mobile")
      margin__120__mobile.classList.remove("space-0-mobile")
      dimensions.style.display ='flex'
      price_table.style.paddingTop = '100px'
    },
    hideSpaceMobile: function() {
      const dimensions = document.querySelector('.dimensions__inner')
      const price_table = document.querySelector('.get-quote__prices')
      var margin__100__mobile = document.querySelector(".btn__oneshipment")
      var margin__0__mobile = document.querySelector(".btn__oneshipment");
      margin__0__mobile.classList.add("space-0-mobile")
      margin__0__mobile.classList.remove("space-100-mobile")
      dimensions.style.display ='none'
      price_table.style.paddingTop = '0px'
        // location.reload()
    },
    manyShipment: function() {
      this.check = false
      window.localStorage.setItem('check', false)
      const tab_one = document.querySelector('.uk-quote')
      const many_shipment = document.querySelector('.many__shipment')
      const tab_many = document.querySelector('.international-quote')
      const one_shipment = document.querySelector('.one__shipment')
      const price_table = document.querySelector('.get-quote__prices')
      many_shipment.style.display ='block'
      one_shipment.style.display = 'none'
      price_table.style.paddingTop = '0px'
      tab_many.style.backgroundColor  = '#00bd64'
      tab_one.style.backgroundColor  = '#2c1f47'
    },
    oneShipment: function() {
      this.check = true
      window.localStorage.setItem('check', true)
      const tab_one = document.querySelector('.uk-quote')
      const many_shipment = document.querySelector('.many__shipment')
      const tab_many = document.querySelector('.international-quote')
      const one_shipment = document.querySelector('.one__shipment')
      const price_table = document.querySelector('.get-quote__prices')
      many_shipment.style.display ='none'
      one_shipment.style.display = 'block'
      tab_many.style.backgroundColor  = '#2c1f47'
      tab_one.style.backgroundColor  = '#00bd64'
    },
    openMenu: function() {
      const btn_menu_show = document.querySelector('.header__menu-open')
      const btn_menu_hide = document.querySelector('.header__menu-close')
      const menu_mobile = document.querySelector('.header__nav')
      menu_mobile.style.display = 'block'
      btn_menu_show.style.display = 'none'
      btn_menu_hide.style.display = 'block'
    },
    closeMenu: function() {
      const btn_menu_show = document.querySelector('.header__menu-open')
      const btn_menu_hide = document.querySelector('.header__menu-close')
      const menu_mobile = document.querySelector('.header__nav')
      menu_mobile.style.display = 'none'
      btn_menu_show.style.display = 'block'
      btn_menu_hide.style.display = 'none'
    },
    hideNotification: function() {
        var btn__close__notif = document.querySelector('.header__icon-close')  
        var notification = document.querySelector('.modal__notification')
        
        notification.style.visibility = 'hidden'
    }
  }
  }
</script>

<style>
    @import '../assets/css/base.css';
    @import '../assets/css/main.css';
    @import '../assets/css/responsive.css';
</style>