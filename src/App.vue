<template>
  <section class="section" id="app">
    <div class="container">
      <div class="columns">
        <div class="raw-course-overview column">
          <div class="field">
            <div class="control">
              <label class="label">Raw course overview</label>
              <textarea class="textarea" placeholder="Raw course overview" rows="10" v-model="rawData" wrap="hard"></textarea>
            </div>
          </div>
        </div>
        <div class="plain-todo-list column">
          <div class="field">
            <div class="control">
              <label class="label">Cleaned-up todo list</label>
              <textarea class="textarea" placeholder="Cleaned-up todo list" rows="10" v-model="cleanedData" wrap="hard"></textarea>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="columns">
        <div class="column is-7 is-offset-5 has-text-right">
          <button class="button is-primary is-outlined">Download Todoist CSV</button>
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
      if (!this.rawData) {
        return '';
      }

      let textBook = this.rawData;
      let reMaps = [
        [
          /\+\n/gm,
          ''
        ],
        [
          /\d+ lectures\n/gm,
          ''
        ],
        [
          /^(\d+:\d+(:\d+)?)/gm,
          '_$1_'
        ],
        [
          /([^\d_])\n/gm,
          '$1 '
        ]
      ];

      for (let index = 0; index < reMaps.length; index++){
        let transliterate = reMaps[index];
        textBook = textBook.replace(transliterate[0], transliterate[1]).trim();
      }

      let lines = textBook.split('\n');
      let linesCounter = lines.length;
      for (let index = 0; index < linesCounter; index++) {
        lines[index] = ['**', index + 1, '/', linesCounter, '** '].join('') + lines[index];
      }

      return lines.join('\n');
    }
  }
};
</script>

<style scoped>
textarea {
  font-family: 'Roboto Mono for Powerline', Monospaced, monospace;
  font-size: 10px;
}
</style>
