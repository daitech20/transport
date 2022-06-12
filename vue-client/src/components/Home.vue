<template>
    <div class="container">
        <form @submit.prevent="createShipment()">
            <div class="row justify-content-center">
                <div class="col-md-5">
                    <h3 class="text-center">From</h3>
                </div>
                <div class="col-md-5">
                    <h3 class="text-center">To</h3>
                </div>
            </div>
          <div class="row justify-content-center">
                <div class="col-lg-4 col-md-10">
                    <input v-model="address.from_street1" type="text" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.username || errors.detail }"
                    placeholder="Street" name="from_street1" />
                </div>
                <div class="col-md-2">
                  <input v-model="address.from_zip" type="text" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.from_error }"
                    placeholder="Zip" name="from_zip" />
                    <div v-if="errors.from_error" class="invalid-feedback">Sai zip</div>
                </div>
                <div class="col-lg-4 col-md-10">
                    <input v-model="address.to_street1" type="text" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.username || errors.detail }"
                    placeholder="Street" name="to_street1" />
                </div>
                <div class="col-md-2">
                  <input v-model="address.to_zip" type="text" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.to_error }"
                    placeholder="Zip" name="to_zip" />
                  <div v-if="errors.to_error" class="invalid-feedback">Sai zip</div>

                </div>
          </div>

          <div class="row justify-content-center">
              <label class="col-sm-0 col-form-label">Length: </label>
              <div class="col-md-2">
                  <input v-model="parcel.length" type="number" step="0.1" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.username || errors.detail }"
                    placeholder="" name="length" />
              </div>
          </div>
            <div class="row justify-content-center">
                <label class="col-sm-0 col-form-label">Width: </label>
              <div class="col-md-2">
                  <input v-model="parcel.width" type="number" step="0.1" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.username || errors.detail }"
                    placeholder="" name="width" />
                </div>
            </div>
            <div class="row justify-content-center">
                <label class="col-sm-0 col-form-label">Height: </label>
              <div class="col-md-2">
                <input v-model="parcel.height" type="number" step="0.1" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.username || errors.detail }"
                    placeholder="" name="height" />
              </div>
            </div>
            <div class="row justify-content-center">
                <label class="col-sm-0 col-form-label">Weight: </label>
              <div class="col-md-2">
                 <input v-model="parcel.weight" type="number" step="0.1" id="form1Example13" class="form-control form-control-lg" :class="{'is-invalid': errors.username || errors.detail }"
                    placeholder="" name="weight" />
              </div>
          </div>

          <div class="row justify-content-center mt-3">
              <button type="submit" class="btn btn-success" >Submit</button>
          </div>
          </form>

          <!-- <div class="col m-4 ">
            {% if has_trans == 0 %}
            <span>No service</span>
            {% else %}
                <table class="table table-hover">
                    <thead>
                        <tr>
                          <th scope="col">Carrier</th>
                          <th scope="col">Service</th>
                          <th scope="col">Price</th>
                            <th scope="col">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for rate in shipment.rates %}
                        <tr data-href="{% url 'core:checkout' rate.shipment_id rate.id %}">
                            <td>{{ rate.carrier }}</td>
                            <td>{{ rate.service }}</td>
                            <td>{{ rate.rate }}</td>
                            <td><button data-href="{% url 'core:checkout' rate.shipment_id rate.id %}" class="btn btn-success" >Select</button></td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div> -->
    </div>
</template>

<script>


import Header from './Header.vue'
const axios = require('axios');
export default {
  components: {
    Header,
  },
  data() {
    return {
      address: {
        from_street1: "",
        from_zip: "",
        from_state: "",
        from_city: "",
        from_country: "",

        to_street1: "",
        to_zip: "",
        to_state: "",
        to_city: "",
        to_country: "",
      },
      parcel: {
        length: "",
        height: "",
        width: "",
        weight: ""
      },
      errors: {
        
      }
    }
  },
  methods: {
    createShipment: function() {
      let from_adress = axios.get(
            'https://ziptasticapi.com/' + this.address.from_zip
      )
      .then(response => {
        if (response.data.error != null) {
          this.errors = {
            "from_error": "sai zip"
          }
          console.log(this.errors)
        }
        else {
          this.errors = {}
          this.address.from_state = response.data.state,
          this.address.from_city = response.data.city,
          this.address.from_country = response.data.country
        }
      })

      let to_address = axios.get(
            'https://ziptasticapi.com/' + this.address.to_zip
      )
      .then(response => {
        if (response.data.error != null) {
          this.errors = {
            "to_error": "sai zip"
          }
          console.log(this.errors)
        }
        else {
          this.errors = {}
          this.address.to_state = response.data.state,
          this.address.to_city = response.data.city,
          this.address.to_country = response.data.country
        }
      })

      console.log(this.address)
      // console.log(to_address)
    }
  }
}
</script>

<style scoped>

</style>