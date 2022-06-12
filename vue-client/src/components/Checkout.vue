<template>
    <div>
        <h1>Checkout</h1>
    </div>
</template>

<script>
    import BaseRequest from '../core/BaseRequest.js'
    export default {
        data() {
            return {

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
                        this.$router.push({name: 'ValidateCustomer'})
                        console.log(verification_code);
                    }
                    
                })
                .catch(() => {
                    this.$router.push({name: 'Login'})
                })
            }
        }
    }
</script>

<style scoped>

</style>