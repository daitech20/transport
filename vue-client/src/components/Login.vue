<template>
    <section class="vh-100">
        <div class="container py-5 h-100">
            <div class="row d-flex align-items-center justify-content-center h-100">
            <div class="col-md-8 col-lg-7 col-xl-6">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg"
                class="img-fluid" alt="Phone image">
            </div>
            <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
                <form @submit.prevent="login()">
                <!-- Email input -->
                <div class="form-outline mb-4">
                    <input v-model="user.username" type="email" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.username || errors.detail }" 
                    placeholder="Enter a email" name="email" />
                    <div v-if="errors.username" class="invalid-feedback">{{ errors.username[0] }}</div>
                    <div v-if="errors.detail" class="invalid-feedback">Sai tài khoản hoặc mật khẩu</div>

                </div>

                <!-- Password input -->
                <div class="form-outline mb-4">
                    <input v-model="user.password" type="password" id="form1Example23" class="form-control form-control-lg" :class="{'is-invalid': errors.password || errors.detail}"
                    placeholder="Enter a password" name="password" />
                    <div v-if="errors.password" class="invalid-feedback">{{ errors.password[0] }}</div>
                </div>

                <div class="d-flex justify-content-around align-items-center mb-4">
                    <!-- Checkbox -->
                    <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="form1Example3" checked />
                    <label class="form-check-label" for="form1Example3"> Remember me </label>
                    </div>
                    <a href="#!">Forgot password?</a>
                </div>

                <!-- Submit button -->
                <button type="submit" class="btn btn-primary btn-lg btn-block">Sign in</button>
                <p class="small fw-bold mt-2 pt-1 mb-0">Don't have an account?
                    <router-link :to="{name: 'Register'}" >
                        <a class="link-danger">Register</a>
                    </router-link>
                </p>
                </form>
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
                    password: ""
                },
                errors: {}

            }
        },
        mounted() {
            this.checkLoggedIn();
        },
        methods: {
            checkLoggedIn: function() {
                let user = window.localStorage.getItem('user');
                BaseRequest.get('user/' + user)
                .then((response) => {
                    console.log(response.data);
                    this.$router.push({name: 'Home'})
                })
                .catch(() => {
                    this.$router.push({name: 'Login'})
                })
            },
            login: function() {
                BaseRequest.post('token/', this.user)
                .then(response => {
                    console.log(response.data);
                    window.localStorage.setItem('token', response.data.access)
                    window.localStorage.setItem('user', response.data.user)
                    window.localStorage.setItem('id', response.data.id)
                    this.$router.push({name: 'Home'})
                })
                .catch(error=> {
                    this.errors = error.response.data
                    console.log("loi");
                    console.log(this.errors);
                });

                // axios.post('http://localhost:8000/api/token/', this.user)
                // .then(response => {
                //     console.log(response.data);
                //     window.localStorage.setItem('token', response.data.access)
                //     window.localStorage.setItem('user', response.data.user)
                //     this.$router.push({name: 'Home'})
                // })
                // .catch(error=> {
                //     this.errors = error.response.data
                //     console.log("loi");
                //     console.log(this.errors);
                // });
            }
        },
    }
</script>

<style scoped>
    .divider:after,
    .divider:before {
    content: "";
    flex: 1;
    height: 1px;
    background: #eee;
    }
</style>