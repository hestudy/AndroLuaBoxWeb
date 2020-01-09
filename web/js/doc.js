var vm = new Vue({
	el: '#app',
	data: {
		doc: null
	},
	methods: {
		onClickLeft() {
			history.back()
		}
	},
	mounted() {
		this.doc = sessionStorage.getItem('doc'),
			console.log(this.doc)
	}
})
