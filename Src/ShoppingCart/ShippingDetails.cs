using System;
using System.Collections.Generic;
using NodaMoney;

namespace ShoppingCart.Controllers
{
    public class ShippingDetails
    {
        public List<DateTime> AvailableSlots { get; set; }
        public Money Cost { get; set; }
    }
}