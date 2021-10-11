$.ajax({
    method: 'GET',
    url: "http://127.0.0.1:8000/api/products/",
    success: function (data) {
        console.log(data)

        for (const obj of data) {
            let card = `<div class="card col-xl-3 col-lg-4 col-md-6 col-sm-12">
                     <img class="card-img-top" src=${obj.photo} alt="Card image cap">
                     <div class="card-body">
                         <h5 class="card-title">${obj.product_name}</h5>
                         <h5 class="card-title card-category">${obj.category}</h5>
                         <p class="card-text">initial price: ${obj.initial_price}</p>
                         <p class="card-text">discount: ${obj.percent}</p>
                         <p class="card-text">final price: ${obj.final_price}</p>
                         <p class="card-text">stock: ${obj.stock}</p>
                         <p class="card-text">description: ${obj.description}</p>
                         <button class="btn btn-primary">add to cart</button>
                     </div>
                </div>`
            $('.product-container').children().children().append(card)
        }

        $('.category-choice').on('click', function () {
            for (const obj of data) {
                // console.log(obj.category)
                // console.log($('.category-choice').value)

                // if (obj.category === $('.category-choice').value) {
                //     console.log(obj.category, $('.category-choice').value)
                // }
            }
        })
    },
    error: function () {
        console.log('error');
    }
})


// import {generate_card} from "./card";
// $('.product-container').children().children().append(generate_card(
//     product_name, category,
//     initial_price, final_price,
//     percent, stock,
//     description,
//     product_img
// ))