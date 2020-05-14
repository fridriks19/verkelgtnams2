$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/computers?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                      if(d.on_sale){
                        d.x = d.discount_price;
                        d.y = d.price
                    } else {
                          d.x = d.price;
                          d.y = ""
                      }
                    return `<div class="single-product"> 
                                <a href="/computers/${d.id}">
                                    <img class="product-img" src="${d.firstImage}"/>
                                    <h4>${d.name}</h4> 
                                    <p>
                                    <del>${d.y}</del>
                                        ${d.x} kr.
                                    </p>
                                </a> 
                            </div>`
                });
                $('.index-product').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error){
                //TODO: GERA BETRI ERROR HANDLE
                console.error(error);
            }
        })
    });
});





