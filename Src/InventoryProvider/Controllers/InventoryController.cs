using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NodaMoney;

namespace InventoryProvider.Controllers
{
    [ApiController]
    [Route("/")]
    public class InventoryController : ControllerBase
    {
        public Task<ProductDetail> GetProductDetails(string productId)
        {
            return Task.FromResult(new ProductDetail
            {
                Name = "abc",
                Price = new Money(15, "USD"),
                ShippingLocation = "Pune"
            });
        }
    }
}
