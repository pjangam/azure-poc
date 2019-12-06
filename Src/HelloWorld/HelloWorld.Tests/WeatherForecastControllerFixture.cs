using System;
using Xunit;
using Moq;
using Microsoft.Extensions.Logging;
using FluentAssertions;

namespace HelloWorld.Tests
{
    public class WeatherForecastControllerFixture
    {
        [Fact]
        public void GivenMockData_WhenUserCallsGet_ThenReturnsSevenDayForcast()
        {
            //given
            var mockLogger=new Mock<ILogger<WeatherForecastController>>();
            var controller = new WeatherForecastController(mockLogger.Object);
            //when
            var forcastData = controller.Get();
            //then
            forcastData.Should().HaveCount(5);
        }
    }
}
