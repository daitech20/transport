<template>
    <div v-if="this.check_Notify == true && this.checkMail == false" class="modal__notification">
        <div class="modal__content">
            <header class="header__notification">
                <span @click="this.hideNotification" class="header__icon-close">
                    <i class="icon__close-notif bi bi-x-lg"></i>
                </span>
            </header>
            <div class="body__notification">
                <h3>Please vetify email to select!!!</h3>
                <h3 style="text-align:center">Click
                    <router-link :to="{name: 'CheckMail'}" >
                        <a href="">this</a>
                    </router-link>
                    to vetify!
                </h3>
            </div>
        </div>
    </div>
    <div v-if="this.check_Notify == true && this.checkLogin == false" class="modal__notification">
        <div class="modal__content">
            <header class="header__notification">
                <span @click="this.hideNotification" class="header__icon-close">
                    <i class="icon__close-notif bi bi-x-lg"></i>
                </span>
            </header>
            <div class="body__notification">
                <h3>Please login to get quote!!!</h3>
                <h3 style="text-align:center">Click 
                    <router-link :to="{name: 'Login'}" >
                        <a href="">this</a>
                    </router-link>
                    to login!
                </h3>
            </div>
        </div>
    </div>
</template>

<script>
    import BaseRequest from '../core/BaseRequest.js'
    export default {
        data() {
            return {
                check_Login: true,
                checkMail: true,
                check_Notify: false
            }
        },
        props: {
            checkLogin: {
                type: Boolean,
                required: true
            },
            check_ValidateEmail: {
                type: Boolean,
                required: true
            },
            checkNotify: {
                type: Boolean,
                required: true
            },
        },
        created() {
            // the prop needs to be re-assigned here. Vue doesn't like prop mutation
            this.checkMail = this.check_ValidateEmail
            this.check_Notify = this.checkNotify
            this.check_Login = this.checkLogin
        },
        updated() {
            this.check_Notify = this.checkNotify
            this.checkMail = this.check_ValidateEmail
            this.check_Login = this.checkLogin
        },
        // mounted() {
        //     this.showNotification
        //     console.log("ab")
        // },
        methods: {          
            hideNotification: function() {
                var btn__close__notif = document.querySelector('.header__icon-close')  
                var notification = document.querySelector('.modal__notification')
                
                this.check_Notify = false
                this.$emit('update:checkNotify', this.check_Notify)
                console.log("ok")
            }
        }
    }
</script>

<style scoped>

</style>