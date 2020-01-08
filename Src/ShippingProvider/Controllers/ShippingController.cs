using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace PaymentProvider.Controllers
{
    [ApiController]
    [Route("/")]
    public partial class ShippingController : ControllerBase
    {
        [HttpGet("/{providerLocation}/{deliveryLocation}")]
        public async Task<List<DateTime>> GetDeliverySlots(string providerLocation, string deliveryLocation)
        {
            var randomizer = new Random();
            return Enumerable.Range(0, randomizer.Next(1, 6))                                   //select min 1 max 6 timeslots
                             .Select(x => DateTime.Now.AddHours(randomizer.Next(12, 72)))   //min 12 max 72 hours from now
                             .ToList();
        }
    }

}
