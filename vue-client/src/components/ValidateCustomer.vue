<template>
    <div>
        <h1>Check mail to validate user</h1>
        <h3>{{$route.params.email}}</h3>
    </div>
</template>

<script>
    import BaseRequest from '../core/BaseRequest.js'
    export default {
        components: {

        },
        data() {
            return {
                errors: {
                    
                }
            }
        },
        mounted() {
            this.checkValidateEmail();
        },
        methods: {
            checkValidateEmail: function() {
                let url = 'validateEmail/' + this.$route.params.email + '/' + this.$route.params.verification_code
                BaseRequest.get(url)
                .then((response) => {
                    console.log(response.data);
                    this.$router.push({name: 'CheckMail', params: { checkMail: true }})
                })
                .catch(error=> {
                    this.errors = error.response.data
                    console.log("loi");
                    console.log(this.errors);
                    this.$router.push({name: 'CheckMail', params: { checkMail: false }})
                })
            }
        }
    }

</script>

<style scoped>

</style>