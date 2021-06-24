<template>
  <div v-if="editor">
    <bubble-menu v-if="editor" :editor="editor">
      <button
        :class="{ 'is-active': editor.isActive('bold') }"
        @click="editor.chain().focus().toggleBold().run()"
      >
        bold
      </button>
      <button
        :class="{ 'is-active': editor.isActive('italic') }"
        @click="editor.chain().focus().toggleItalic().run()"
      >
        italic
      </button>
      <button
        :class="{ 'is-active': editor.isActive('strike') }"
        @click="editor.chain().focus().toggleStrike().run()"
      >
        strike
      </button>
    </bubble-menu>
    <editor-content :editor="editor" />
  </div>
</template>

<script>
import { Editor, EditorContent, BubbleMenu } from '@tiptap/vue-2'
import StarterKit from '@tiptap/starter-kit'
import VueComponent from './QuestionWithAnswer'
import TableOfContents from './TableOfContent'

export default {
  components: {
    EditorContent,
    BubbleMenu,
  },
  props: {
    value: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      editor: null,
    }
  },
  watch: {
    value(value) {
      const isSame = this.editor.getHTML() === value

      if (isSame) {
        return
      }

      this.editor.commands.setContent(this.value, false)
    },
  },

  beforeDestroy() {
    this.editor.destroy()
  },
  mounted() {
    this.editor = new Editor({
      extensions: [StarterKit, VueComponent, TableOfContents],
      content: this.value,
      onUpdate: () => {
        this.$emit('input', this.editor.getHTML())
      },
    })
  },
}
</script>

<style lang="scss">
/* Basic editor styles */
.ProseMirror {
  > * + * {
    margin-top: 0.75em;
  }
}
</style>
