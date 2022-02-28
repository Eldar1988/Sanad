<template>
  <q-page>
    <page-header title="Прайс-лист" back-u-r-l="/" back-route-button/>
    <section class="container-m">
      <q-table
        square flat bordered
        class="my-sticky-virtscroll-table q-mt-md"
        :data="price"
        :columns="columns"
        style="height: 500px"
        row-key="name"
        hide-pagination
        virtual-scroll
        :virtual-scroll-sticky-size-start="48"
        :pagination.sync="pagination"
        :rows-per-page-options="[0]"
      >

        <template v-slot:header="props">
          <div :props="props" class="row no-wrap grey-gradient" style="min-width: 700px; overflow-x: scroll">
            <div
              v-for="col in props.cols"
              :key="col.name"
              :props="props"
              class="text-uppercase q-pa-md text-bold"
              :class="col.class"
            >
              {{ col.label }}
            </div>
          </div>
        </template>

        <template v-slot:body="props">
          <div :props="props" class="row no-wrap data-row items-center">
            <div :props="props" key="name" class="col-3 q-pa-md text-subtitle1 flex justify-between no-wrap">
              <div>{{ props.row.title }}</div>
              <q-btn
                v-if="props.row.direction"
                :to="`/direction/${props.row.direction.slug}`"
                icon="las la-external-link-alt"
                dense flat
                title="Узнать подробнее"
              />
            </div>
            <div :props="props" key="description" class="col-7 q-pa-md">
              {{ props.row.text }}
            </div>
            <div :props="props" key="price" class="col-2 q-pa-md text-subtitle1 text-bold">
              {{ formattedPrice(props.row.price) }} тг
            </div>
          </div>
        </template>
      </q-table>
    </section>

    <page-footer />
  </q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import PageFooter from "components/footer/page-footer";

export default {
  name: "Price",
  components: {PageFooter, PageHeader},
  computed: {
    price() {
      return this.$store.getters.getPrice
    }
  },
  methods: {
    formattedPrice (price) {
      return new Intl.NumberFormat('ru', {}).format(price)
    }
  },
  data() {
    return {
      pagination: {
        rowsPerPage: 0
      },
      columns: [
        {
          name: 'name',
          required: true,
          label: 'Услуга',
          align: 'left',
          class: 'col-3',
          style: 'width: 30% !important'
        },
        {
          name: 'description',
          align: 'center',
          label: 'Описание',
          field: 'description',
          class: 'col-7',
          style: 'max-width: 400px !important'
        },
        {
          name: 'price',
          align: 'center',
          label: 'Цена',
          field: 'price',
          class: 'col-2',
          style: 'width: 20% !important'
        }
      ]
    }
  },
  preFetch({store}) {
    return store.dispatch('loadPrice')
  }
}
</script>

<style lang="sass">
.data-row:nth-child(even)
  background: $grey-2

::-webkit-scrollbar
  width: 3px /* ширина для вертикального скролла */
  height: 0 /* высота для горизонтального скролла */
  background-color: #fff

::-webkit-scrollbar-thumb
  background-color: $grey-4
.my-sticky-header-column-table
  /* height or max-height is important */

  /* specifying max-width so the example can
    highlight the sticky column on any browser window */
  max-width: 100%

  td:first-child
    /* bg color is important for td; just specify one */
    background-color: $info !important

  tr th
    position: sticky
    /* higher than z-index for td below */
    z-index: 2
    /* bg color is important; just specify one */
    background: #fff

  /* this will be the loading indicator */

  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
    /* highest z-index */
    z-index: 3

  thead tr:first-child th
    top: 0
    z-index: 1

  tr:first-child th:first-child
    /* highest z-index */
    z-index: 3

  td:first-child
    z-index: 1
</style>

<style lang="sass">
.my-sticky-virtscroll-table
  /* height or max-height is important */
  height: 410px

  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th /* bg color is important for th; just specify one */
    background-color: #fff

  thead tr th
    position: sticky
    z-index: 1
  /* this will be the loading indicator */
  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
  thead tr:first-child th
    top: 0
</style>
