<template>
  <section class="section" id="app">
    <div class="container">
      <div class="columns">
        <div class="raw-course-overview column">
          <div class="field">
            <div class="control">
              <label class="label">Raw course overview</label>
              <textarea class="textarea" placeholder="Raw course overview" rows="10" v-model="rawData"></textarea>
            </div>
          </div>
        </div>
        <div class="plain-todo-list column">
          <div class="field">
            <div class="control">
              <label class="label">Cleaned-up todo list</label>
              <textarea class="textarea" placeholder="Cleaned-up todo list" rows="10" v-model="cleanedData"></textarea>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="columns">
        <div class="column is-7 is-offset-5 has-text-right">
          <button class="button is-primary is-outlined">Download Todoist template</button>
          <button class="button is-link is-outlined">Preview</button>
          <button class="button is-info is-outlined" title="">Create Todoist project</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      rawData: ''
    }
  },
  computed: {
    cleanedData() {

      return 'XXXX';
    }
  }
};
</script>
