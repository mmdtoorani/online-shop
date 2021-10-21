$.ajax({
    method: 'GET',
    url: '/api/products/categories/',
    success: function (categories) {
        console.log(categories)
        for (const cat of categories) {
            let cat_name = cat.category_name;
            let cat_link = `<button class="btn category-choice" value="${cat_name}"> ${cat_name}</button>`

            let cat_btn = $('#navbarSupportedContent').append(cat_link);
        }
        // cat_btn.on('click', function () {
        //     console.log('cat_link clicked')
        // })
    },
    error: function () {
        console.log('error in get data from category api!')
    }
})


// $.ajax({
//     method: 'GET',
//     url: 'http://127.0.0.1:8000/api/products/',
//     success: function (products) {
//         for (const product of products) {
//             let product_name = product.product_name;
//             let category = product.category;
//             let initial_price = product.initial_price;
//             let final_price = product.final_price;
//             let percent = product.percent;
//             let stock = product.stock;
//             let description = product.description;
//             let category_in_prdctAPI = product.category
//             if (category_in_prdctAPI === category_in_prdctAPI) {
//                 // let card = generate_card(
//                 //     product_name, category,
//                 //     initial_price, final_price,
//                 //     percent, stock, description
//                 // )
//                 $('.product-container').children().children().empty().append(
//                     `<div class="card col-xl-3 col-lg-4 col-md-6 col-sm-12">
//                                      <img class="card-img-top" src=${product_img} alt="Card image cap">
//                                      <div class="card-body">
//                                          <h5 class="card-title">${product_name}</h5>
//                                          <h5 class="card-title">category: ${category}</h5>
//                                          <p class="card-text">initial price: ${initial_price}</p>
//                                          <p class="card-text">discount: ${percent}</p>
//                                          <p class="card-text">final price: ${final_price}</p>
//                                          <p class="card-text">stock: ${stock}</p>
//                                          <p class="card-text">description: ${description}</p>
//                                          <button class="btn btn-primary">add to cart</button>
//                                      </div>
//                                 </div>`)
//                 // import {generate_card} from "./card";
//             }
//         }
//     }
// }