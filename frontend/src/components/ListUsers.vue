<template>
    <div class="container">
        <div class="row justify-content-center">
          <div class="col col-4">
            <v-select multiple v-model="selected" :options="options" :reduce="name => name.code" label="name" />
          </div>
          <div class="col col-1">
            <button type="button" class="btn btn-primary" @click="fetchUsers()">Refresh</button>
          </div>
        </div>
        <div class="row mt-4">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Gender</th>
                <th scope="col">Email</th>
                <th scope="col">Country</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user.name">
                <td>{{user.name}}</td>
                <td>{{user.gender}}</td>
                <td>{{user.email}}</td>
                <td>{{user.country}}</td>
              </tr>
              <tr v-if="users.length==0">
                <td colspan="4">No Data!</td>
              </tr>
            </tbody>
          </table>
        </div>

    </div>
</template>
  
<script>
  import vSelect from 'vue-select'
  import countries from './countries.json'

  export default {
    name: 'ListUsers',
    components: {
      vSelect
    },
    created() {
      this.fetchUsers()
    },
    data() {
      return {
        selected: [],
        options: countries,
        users: [],
        countries: []
      }
    },
    methods: {
      async fetchUsers() {
        const response = await fetch(`http://127.0.0.1:8000/api/users?countries=${this.selected.join()}`)
        const data = await response.json()
        this.countries = data.countries
        this.users = []

        this.setUserData(this.countries)

      },
      setUserData(data) {
        data.map(
          (country)=>{
            let user = country.users.map(
              (user)=>{
                user.country = country.name
                this.users.push(user)
              })
          })
      }
    }
  }
</script>