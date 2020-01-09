var vm = new Vue({
	el: '#app',
	data: {
		active: 0,
		contentdata: null,
		loading: true
	},
	methods: {
		ondoc(key) {
			sessionStorage.setItem('content', JSON.stringify(key)),
				window.location.assign('content.html')
		}
	},
	mounted() {
		axios
			.get('http://103.72.146.159:1111/api/')
			.then(response => (
				this.contentdata = response.data,
				this.loading = false
			))
			.catch(function(error) { // 请求失败处理
				console.log(error);
			});
	}
})
