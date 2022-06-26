<template>
    <header class="header sticky-footer__header">
        <div class="containers">
            <router-link :to="{name: 'Home'}" >
                <img class="header__logo" src="../assets/img/logo.png" alt="">
            </router-link>
            <nav class="header__nav">
                <ul class="header__menu">
                    <li class="header__menu-item header__menu-home">
                        <router-link :to="{name: 'Home'}">
                        <a href=""><i class="fa-solid bi bi-house"></i></a>
                        </router-link>
                    </li>
                    <li class="header__menu-item header__menu-tracking">
                        <a class="header__link" href="/">Tracking</a>
                        <div class="header__tracking">
                            <input class="track__input" type="text" placeholder="PM_#######_#######">
                            <button type="submit" class="track__btn">Track Now</button>
                        </div>
                    </li>
                    <li class="header__menu-item header__menu-contact">
                        <a class="header__link" href="/">Contact Us</a>
                    </li>
                    <li v-if="this.checkLogin==false" class="header__menu-item header__menu-signup">
                        <router-link :to="{name: 'Register'}" style="text-decoration: none">
                            <span class="header__link">Sign Up</span>
                        </router-link>
                    </li>
                    <li v-if="this.checkLogin==false" class="header__menu-item header__menu-login">
                        <router-link :to="{name: 'Login'}" style="text-decoration: none">
                            <span class="header__link">Log In</span>
                        </router-link>
                    </li>
                    <li v-if="this.checkLogin" class="header__menu-item header__menu-avatar">
                        <img class="header-avatar" src="../assets/img/avatar.jpg" alt="">
                        <ul class="header__menu-item-submenu">
                            <li class="header__menu-item-submenu-link">
                                <a class="header__link" href="/">DashBoard</a>
                            </li>
                            <li class="header__menu-item-submenu-link">
                                <a class="header__link" style="cursor: pointer" @click="this.Logout">Log Out</a>
                            </li>
                    </ul>
                    </li>
                </ul>
            </nav>
            <div class="header__open-menu">
                <span class="header__menu-icon header__menu-open" @click="openMenu">
                    <i class="bi bi-list fa-solid fa-bars"></i>
                </span>
                <span class="header__menu-close" @click="closeMenu">
                    <i class="bi bi-x-lg fa-solid fa-xmark" style="color:white"></i>
                </span>
            </div>
        </div>
    </header>
</template>

<script>
    import BaseRequest from '../core/BaseRequest.js'
    export default {
        data() {
            return {
                checkLogin: false
            }
        },
        mounted() {
            this.checkLoggedIn()
        },
        updated() {
            this.checkLoggedIn()
        },
        props: {
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
            Logout: function() {
                window.localStorage.clear()
                this.checkLogin = false
                this.$router.push({ name: 'Login'})
            }
        }
    }
</script>

<style scoped>

</style>