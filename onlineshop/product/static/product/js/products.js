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

            let card = generate_card(product_name, category, initial_price, final_price, percent, stock, description)
            import {generate_card} from "./card";
            $('.product-container').children().children().append(card)
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
