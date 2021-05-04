<template>
<div class="h-100 w-full flex items-center justify-center bg-teal-lightest font-sans">
	<div class="bg-white rounded shadow p-6 m-4 w-full lg:w-3/4 lg:max-w-lg">
    <div class="mb-4">
       <Headers />
       <Form />
    </div>
  </div>
</div>
</template>

<script>
import Headers from '@/components/Headers.vue'
import Form from '@/components/Form.vue'

export default {
  name: 'App',
  components: {
    Headers,
    Form,
  }
}
</script>


