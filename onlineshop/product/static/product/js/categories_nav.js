$.ajax({
    method: 'GET',
    url: 'http://127.0.0.1:8000/api/products/categories/',
    success: function (data) {
        console.log(data)
        for (const obj of data) {
            let category = obj.category_name

            let cat_link = `<button class="btn"> ${category}</button>`
            $('#navbarSupportedContent').append(cat_link).on('click', function() {

            })
        }
    },
    error: function () {
        console.log('error in get data from category api!')
    }
})