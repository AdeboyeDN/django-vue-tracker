<template>
     <form @submit.prevent="addTask"  class="flex mt-4" >
          <input v-model="pageTitle"    class="shadow appearance-none border rounded w-full py-2 px-3 mr-4 text-grey-darker" placeholder="Add Todo">
          <button class="flex-no-shrink p-2 border-2 rounded text-teal border-teal hover:text-white hover:bg-teal">Add</button>
     </form>
</template>

<script>
export default {
     name : "Form",
     data() {
        title: ''
        done: false
        date: '20,august'
     },
     methods: {
          addTask() {
               this.title == pageTitle
               alert(this.title)
          },

     }
     
}
</script>

