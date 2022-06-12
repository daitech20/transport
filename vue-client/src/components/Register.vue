<template>
    <section class="h-100 bg-dark">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col">
                <div class="card card-registration my-4">
                <div class="row g-0">
                    <div class="col-xl-6 d-none d-xl-block">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/img4.webp"
                        alt="Sample photo" class="img-fluid"
                        style="border-top-left-radius: .25rem; border-bottom-left-radius: .25rem;" />
                    </div>
                    <div class="col-xl-6">
                    <form @submit.prevent="register()">
                        <div class="card-body p-md-5 text-black">
                            <h3 class="mb-5 text-uppercase">Customer registration form</h3>

                            <div class="row">
                            <div class="col-md-6 mb-4">
                                <div class="form-outline">
                                <input v-model="user.first_name" type="text" id="form3Example1m" class="form-control form-control-lg" placeholder="First Name" name="first_name" />
                                </div>
                            </div>
                            <div class="col-md-6 mb-4">
                                <div class="form-outline">
                                <input v-model="user.last_name" type="text" id="form3Example1n" class="form-control form-control-lg" placeholder="Last Name" name="last_name" />
                                </div>
                            </div>
                            </div>

                            <div class="form-outline mb-4">
                                <input v-model="address.street1" type="text" id="form3Example8" class="form-control form-control-lg" placeholder="Street" name="street1" />
                            </div>

                            <div class="form-outline mb-4">
                                <input v-model="user.username" type="text" id="form1Example13" class="form-control form-control-lg" placeholder="Enter a username" name="username" :class="{'is-invalid': errors.username}" />
                                <div v-if="errors.username" class="invalid-feedback">Tên tài khoản đã tồn tại!</div>
                            </div>

                            <div class="form-outline mb-4">
                                <input v-model="user.password" type="password" id="form1Example13" class="form-control form-control-lg" placeholder="Password" name="password" :class="{'is-invalid': errors.error}" />
                                    <div v-if="errors.error" class="invalid-feedback">{{ errors.error[0] }}</div>
                            </div>

                            <div class="form-outline mb-4">
                                <input v-model="user.password2" type="password" id="form1Example13" class="form-control form-control-lg" placeholder="Repeat your Password" name="password2" :class="{'is-invalid': errors.error}" />
                                <div v-if="errors.error" class="invalid-feedback">{{ errors.error[0] }}</div>
                            </div>

                            <div class="form-outline mb-4">
                                <input v-model="user.email" type="email" id="form1Example13" class="form-control form-control-lg" placeholder="Enter a email" name="email" :class="{'is-invalid': errors.email}"/>
                                <div v-if="errors.email" class="invalid-feedback">Email đã tồn tại!</div>
                            </div>

                            <div class="col-md-3 mb-4">
                                <div class="form-outline mb-4">
                                    <input v-model="address.zip" type="text" id="form3Example90" class="form-control form-control-lg" placeholder="Zipcode" name="zip" />
                                </div>
                            </div>

                            <div class="d-flex justify-content-end pt-3">
                            <button @click="resetAll()" type="button" class="btn btn-light btn-lg">Reset all</button>
                            <button type="submit" class="btn btn-warning btn-lg ms-2">Submit form</button>
                            </div>
                        </div>
                    </form>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        </section>
</template>

<script>
    import BaseRequest from '../core/BaseRequest.js'
    export default {
        data() {
            return {
                user: {
                    username: "",
                    email: "",
                    password: "",
                    password2: "",
                    first_name: "",
                    last_name: "",
                },
                address: {
                    street1: "",
                    zip: ""
                },
                errors: {}
            }
        },
        methods: {
            register: function() {
                BaseRequest.post('register/', this.user)
                .then(response => {
                    console.log(response.data);
                    window.localStorage.setItem('user', response.data.username)
                    this.$router.push({name: 'ValidateCustomer'})
                })
                .catch(error=> {
                    this.errors = error.response.data
                    console.log("loi");
                    console.log(this.errors);
                });

            },
            resetAll: function() {
                this.user = {
                    username: "",
                    email: "",
                    password: "",
                    password2: "",
                    first_name: "",
                    last_name: "",
                },
                this.address = {
                    street1: "",
                    zip: ""
                },
                this.errors = {},

                console.log(this.user)
            }
        }
    }
</script>

<style scoped>
    .card-registration .select-input.form-control[readonly]:not([disabled]) {
        font-size: 1rem;
        line-height: 2.15;
        padding-left: .75em;
        padding-right: .75em;
    }
    .card-registration .select-arrow {
    top: 13px;
    }
</style>>