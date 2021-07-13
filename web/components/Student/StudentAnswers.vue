<template>
  <c-box>
    <c-flex my="10" direction="row" justify="space-between" align="center">
      <c-text font-size="30px">Book's name</c-text>
      <c-button variant-color="blue">Submission</c-button>
    </c-flex>
    <c-box
      class="scrollbar"
      border="1px"
      border-color="gray.200"
      height="750px"
      mb="10"
      p="5"
      overflow-y="auto"
    >
      <c-list>
        <c-list-item
          v-for="(item, index) in items"
          :id="index"
          :key="index"
          margin-bottom="10px"
        >
          <c-box v-if="item.type === 'multiple'">
            <c-text>{{ index + 1 }}&#8228;&nbsp; {{ item.question }}</c-text>
            <c-stack>
              <c-radio-group is-inline>
                <c-radio
                  v-for="answer in item.answers"
                  :key="answer.id"
                  v-model="answer.value"
                  :name="answer.text"
                  :value="answer.id"
                  px="5"
                  py="2"
                >
                  {{ answer.text }}
                </c-radio>
              </c-radio-group>
            </c-stack>
            <student-comment />
          </c-box>
          <c-box v-else>
            <c-text>{{ index + 1 }}&#8228;&nbsp; {{ item.question }}</c-text>
            <c-flex mb="3">
              <c-text pl="5" pr="3">Answer&#58;</c-text>
              <c-text>{{ item.answer }}</c-text>
            </c-flex>
            <student-points mb="3" />
            <student-comment />
          </c-box>
        </c-list-item>
      </c-list>
    </c-box>
  </c-box>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          type: 'multiple',
          question: 'What is Lorem Ipsum?',
          answers: [
            {
              id: 1,
              text: 'A. HTML',
              value: '',
            },
            {
              id: 2,
              text: 'B. C/C++',
              value: '',
            },
            {
              id: 3,
              text: 'C. Javascipt',
              value: '',
            },
            {
              id: 4,
              text: 'D. C#',
              value: '',
            },
          ],
        },
        {
          type: 'multiple',
          question: 'What is Lorem Ipsum?',
          answers: [
            {
              id: 1,
              text: 'A. HTML',
              value: '',
            },
            {
              id: 2,
              text: 'B. C/C++',
              value: '',
            },
            {
              id: 3,
              text: 'C. Javascipt',
              value: '',
            },
            {
              id: 4,
              text: 'D. C#',
              value: '',
            },
          ],
        },
        {
          type: 'essay',
          question: 'Where does it come from?',
          answer:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries.",
        },
        {
          type: 'multiple',
          question: 'What is Lorem Ipsum?',
          answers: [
            {
              id: 1,
              text: 'A. HTML',
              value: '',
            },
            {
              id: 2,
              text: 'B. C/C++',
              value: '',
            },
            {
              id: 3,
              text: 'C. Javascipt',
              value: '',
            },
            {
              id: 4,
              text: 'D. C#',
              value: '',
            },
          ],
        },
        {
          type: 'essay',
          question: 'Where does it come from?',
          answer:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries.",
        },
        {
          type: 'essay',
          question: 'Where does it come from?',
          answer:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries.",
        },
        {
          type: 'essay',
          question: 'Where does it come from?',
          answer:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries.",
        },
      ],
    }
  },
}
</script>

<style scoped>
.scrollbar::-webkit-scrollbar {
  display: none;
}
</style>
