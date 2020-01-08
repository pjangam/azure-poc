using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace InventoryProvider.Controllers
{
    [ApiController]
    [Route("/")]
    public class InventoryController : ControllerBase
    {
        [HttpGet("{productId}")]
        public Task<ProductDetail> GetProductDetails(string productId)
        {
            return Task.FromResult(new ProductDetail
            {
                Name = "abc",
                Price = new Money( "USD",15),
                ShippingLocation = "Pune"
            });
        }
    }
}
