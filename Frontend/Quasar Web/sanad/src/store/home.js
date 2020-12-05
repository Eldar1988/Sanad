const serverURL = 'http://192.168.0.199:8000'

export const actions = {
  async fetchHomePageData () {
    try {
      const homeProducts = await this.$axios.$get(`${serverURL}/get_home_page_data`)
      return homeProducts
    } catch {}
  }
}
