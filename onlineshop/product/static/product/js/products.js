$.ajax({
    method: 'GET',
    url: "http://127.0.0.1:8000/api/products/",
    success: function (data) {
        console.log('success');
        console.log(data)

        for (const obj of data) {
            let product_name = obj.product_name;
            let category = obj.category;
            let initial_price = obj.initial_price;
            let final_price = obj.final_price;
            let percent = obj.percent;
            let stock = obj.stock;
            let description = obj.description;
            const card =
                `<div class="card" style="width: 18rem;">
                     <img class="card-img-top" src=${obj.photo} alt="Card image cap">
                     <div class="card-body">
                         <h5 class="card-title">${product_name}</h5>
                         <p class="card-text">${initial_price}</p>
                         <p class="card-text">${percent}</p>
                         <p class="card-text">${final_price}</p>
                         <p class="card-text">${stock}</p>
                         <p class="card-text">${description}</p>
                         <button class="btn btn-primary">add to cart</button>
                     </div>
                </div>`;
            $('.product-container').append(card)
        }
    },
    error: function () {
        console.log('error');
    }
})


//


// $.ajax({
//     method: 'GET',
//     url: "http://127.0.0.1:8000/api/products/categories/",
//     success: function (categories) {
//         console.log('success in categories')
//         console.log(categories)
//
//         for (const category of categories) {
//             const category_name = category.category_name
//         }
//
//     }
// })
