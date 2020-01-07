using NodaMoney;

namespace InventoryProvider.Controllers
{
    public class ProductDetail
    {
        public Money Price { get; set; }
        public string Name { get; set; }
        public string ShippingLocation { get; set; }
    }
}
