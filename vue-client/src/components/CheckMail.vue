<template>
    <Header />
    <div class="content">
        <div v-if="this.checkMail == false && this.check == false" class="home">
            <h1>Vui lòng kiểm tra gmail để xác nhận!!!</h1>
            <h2>Nếu chưa có bấm vào 
                <button type="button" class="btn btn-danger" @click="this.sendMail">đây</button>
                để gửi lại mã.
            </h2>
            <h3 v-if="this.notifi">
                Kiểm tra mail của bạn
            </h3>
        </div>
        <div v-if="this.checkMail == true || this.check == true" class="home">
            <h1>Account verification successful!!!</h1>
            <h2>Click 
                <router-link :to="{name: 'Home'}">
                    <a href="">this</a> 
                </router-link>
                to go Home.
            </h2>
        </div>
    </div>
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
                errors: {
                    
                },
                check: false,
                notifi: false,
            }
        },
        props: {
            checkMail: {
                type: Boolean,
                required: true
            }
        },
        mounted() {
            this.checkLoggedIn();
            this.checkValidateEmail();
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
                        console.log(verification_code);
                        this.check = false
                    }
                    else {
                        this.check = true
                    }
                    
                })
                .catch(() => {
                    console.log("error")
                })
            },
            sendMail: function() {
                console.log("send mai")
                let username = window.localStorage.getItem('user')
                BaseRequest.get('sendMail/' + username)
                .then((response) => {
                    console.log(response.data)
                    this.notifi = true
                })
                .catch(() => {
                    console.log("error")
                })
            }
        }
    }

</script>

<style scoped>
    .content{
    height:75vh;
    background-image:linear-gradient(to right,#8059e8, #47288d) ;
    position: relative;
    }
    

    .home{
        position: absolute;
        text-align: center;
        top: 50%;
        transform: translate(-50%, -50%);
        left: 50%;
        width: 100%;
    }

    .home h1{
        margin: 0;
        font-size: 2.8em;
        color: #fff;
        padding: 20px 0;
    }

    .home h2{
        font-size: 2.4em;
        color: #fff;
    }

    .home h2 a{
        color: #000;
    }

</style>