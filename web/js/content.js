var vm = new Vue({
	el: '#app',
	data: {
		contentdata: null
	},
	methods: {
		todoc(data) {
			sessionStorage.setItem('doc', data),
				window.location.assign('doc.html')
		},
		onClickLeft() {
			history.back()
		}
	},
	mounted() {
		this.contentdata = JSON.parse(sessionStorage.getItem('content'))
	}
})
