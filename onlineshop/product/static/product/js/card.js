export function generate_card(name, category, initial_price, final_price, percent, stock, description) {
    return `<div class="card col-xl-3 col-lg-4 col-md-6 col-sm-12" style="100%">
                     <img class="card-img-top" src=${obj.photo} alt="Card image cap">
                     <div class="card-body">
                         <h5 class="card-title">${name}</h5>
                         <p class="card-text">${initial_price}</p>
                         <p class="card-text">${percent}</p>
                         <p class="card-text">${final_price}</p>
                         <p class="card-text">${stock}</p>
                         <p class="card-text">${description}</p>
                         <button class="btn btn-primary">add to cart</button>
                     </div>
                </div>`
}
