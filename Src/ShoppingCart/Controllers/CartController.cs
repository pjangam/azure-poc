using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace ShoppingCart.Controllers
{
    [ApiController]
    [Route("/")]
    public class CartController : ControllerBase
    {
        private readonly InventoryServiceAdaptor _inventory;
        private readonly ShippingServiceAdaptor _shipping;

        public CartController(InventoryServiceAdaptor inventory, ShippingServiceAdaptor shipping)
        {
            this._shipping = shipping;
            this._inventory = inventory;

        }
        [HttpPost]
        public async Task<ShippingDetails> Checkout(string productId, string deliveryLocation)
        {
            var productDetail = await _inventory.GetProductDetails(productId);
            var slots = await _shipping.GetDeliverySlots(productDetail.ShippingLocation, deliveryLocation);
            return new ShippingDetails
            {
                Cost = productDetail.Price,
                AvailableSlots = slots
            };
        }
    }
}
