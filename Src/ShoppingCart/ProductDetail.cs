using NodaMoney;

namespace ShoppingCart.Controllers
{
    public class ProductDetail
    {
        public Money Price { get; set; }
        public string Name { get; set; }
        public string ShippingLocation { get; set; }
    }
}