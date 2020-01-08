using System;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace ShoppingCart.Controllers
{
    public class InventoryServiceAdaptor
    {
        private readonly string _url;
        public InventoryServiceAdaptor()
        {
            this._url = Environment.GetEnvironmentVariable("inventoryServiceUrl") ?? "http://localhost:5010";
        }
        public async Task<ProductDetail> GetProductDetails(string productId)
        {
            System.Console.WriteLine($"{_url}/{productId}");
            var productDetailString = await Helper.GetAsync($"{_url}/{productId}");
            return JsonConvert.DeserializeObject<ProductDetail>(productDetailString);
        }
    }
}