<template>
  <div v-if="editor" class="ProseMirror border border-gray-200">
    <bubble-menu v-if="editor" class="bubble-menu" :editor="editor">
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
import tippy from 'tippy.js'
import { Editor, EditorContent, BubbleMenu, VueRenderer } from '@tiptap/vue-2'
import StarterKit from '@tiptap/starter-kit'
import Heading from '@tiptap/extension-heading'
import VueComponent from './QuestionWithAnswer'
import TableOfContents from './TableOfContent'
import SlashCommands from './SlashCommand'
import SlashComponent from './SlashCommand/Component.vue'

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
      extensions: [
        StarterKit,
        VueComponent,
        TableOfContents,
        Heading.configure({ level: [1, 2, 3] }),
        SlashCommands.configure({
          suggestion: {
            items: (query) => {
              return [
                {
                  title: 'H1',
                  command: ({ editor, range }) => {
                    editor
                      .chain()
                      .focus()
                      .deleteRange(range)
                      .setNode('heading', { level: 1 })
                      .run()
                  },
                },
                {
                  title: 'H2',
                  command: ({ editor, range }) => {
                    editor
                      .chain()
                      .focus()
                      .deleteRange(range)
                      .setNode('heading', { level: 2 })
                      .run()
                  },
                },
                {
                  title: 'bold',
                  command: ({ editor, range }) => {
                    editor
                      .chain()
                      .focus()
                      .deleteRange(range)
                      .setMark('bold')
                      .run()
                  },
                },
                {
                  title: 'italic',
                  command: ({ editor, range }) => {
                    editor
                      .chain()
                      .focus()
                      .deleteRange(range)
                      .setMark('italic')
                      .run()
                  },
                },
              ]
                .filter((item) =>
                  item.title.toLowerCase().startsWith(query.toLowerCase())
                )
                .slice(0, 10)
            },
            render: () => {
              let component
              let popup

              return {
                onStart: (props) => {
                  component = new VueRenderer(SlashComponent, {
                    parent: this,
                    propsData: props,
                  })

                  popup = tippy('body', {
                    getReferenceClientRect: props.clientRect,
                    appendTo: () => document.body,
                    content: component.element,
                    showOnCreate: true,
                    interactive: true,
                    trigger: 'manual',
                    placement: 'bottom-start',
                  })
                },
                onUpdate(props) {
                  component.updateProps(props)

                  popup[0].setProps({
                    getReferenceClientRect: props.clientRect,
                  })
                },
                onKeyDown(props) {
                  return component.ref?.onKeyDown(props)
                },
                onExit() {
                  popup[0].destroy()
                  component.destroy()
                },
              }
            },
          },
        }),
      ],
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
.ProseMirror:focus-visible {
  outline: none;
}

h1 {
  display: block;
  font-size: 2em;
  font-weight: semi-bold;
}

h2 {
  display: block;
  font-size: 1.5em;
  font-weight: semi-bold;
}

.bubble-menu {
  display: flex;
  background-color: #0d0d0d;
  padding: 0.4rem;
  border-radius: 0.5rem;

  button {
    border: none;
    background: none;
    color: #fff;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0 0.4rem;

    &:hover,
    &.is-active {
      color: #a975ff;
    }
  }
}
</style>
