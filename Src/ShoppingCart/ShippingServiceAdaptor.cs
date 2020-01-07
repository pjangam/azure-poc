using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace ShoppingCart.Controllers
{
    public class ShippingServiceAdaptor
    {
        private readonly string _url;
        public ShippingServiceAdaptor()
        {
            this._url = Environment.GetEnvironmentVariable("shippingServiceUrl") ?? "http://localhost:5030";
        }
        //public async Task<ProductDetail> GetProductDetails(string productId)
        public async Task<List<DateTime>> GetDeliverySlots(string providerLocation, string deliveryLocation)
        {
            var productDetailString = await Helper.GetAsync($"_url/{providerLocation}/{deliveryLocation}");
            return JsonConvert.DeserializeObject<List<DateTime>>(productDetailString);
        }



        // public async Task<List<DateTime>> GetDeliverySlots(string providerLocation, string deliveryLocation)
        // {
        //     var randomizer = new Random();
        //     return Enumerable.Range(0, randomizer.Next(1, 6))                                   //select min 1 max 6 timeslots
        //                      .Select(x => DateTime.Now.AddHours(randomizer.Next(12, 72)))   //min 12 max 72 hours from now
        //                      .ToList();
        // }
    }
}