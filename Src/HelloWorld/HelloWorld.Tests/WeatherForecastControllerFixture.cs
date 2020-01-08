using System;
using Xunit;
using Moq;
using Microsoft.Extensions.Logging;
using FluentAssertions;
using System.Threading.Tasks;
using Newtonsoft.Json;
using ShoppingCart.Controllers;

namespace HelloWorld.Tests
{
    public class WeatherForecastControllerFixture
    {
        [Fact]
        public void GivenMockData_WhenUserCallsGet_ThenReturnsSevenDayForcast()
        {
            //given
            var mockLogger = new Mock<ILogger<WeatherForecastController>>();
            var controller = new WeatherForecastController(mockLogger.Object);
            //when
            var forcastData = controller.Get();
            //then
            forcastData.Should().HaveCount(5);
        }


        [Fact]
        public async Task TestDeserialization()
        {
            var str = "{\"price\":{\"amount\":15,\"currency\":{\"symbol\":\"$\",\"englishName\":\"United States dollar\",\"code\":\"USD\",\"number\":\"840\",\"namespace\":\"ISO-4217\",\"decimalDigits\":2,\"majorUnit\":1,\"minorUnit\":0.01,\"isObsolete\":false}},\"name\":\"abc\",\"shippingLocation\":\"Pune\"}";
            var settings = new JsonSerializerSettings
            {
                NullValueHandling = NullValueHandling.Ignore,
                MissingMemberHandling = MissingMemberHandling.Ignore
            };
            var x = JsonConvert.DeserializeObject<ProductDetail>(str, settings);
            System.Console.WriteLine(x);

        }
    }
}
