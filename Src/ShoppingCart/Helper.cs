using System;
using System.IO;
using System.Net;
using System.Threading.Tasks;

namespace ShoppingCart
{
    public class Helper
    {
        public static async Task<string> GetAsync(string uri)
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uri);
            request.AutomaticDecompression = DecompressionMethods.GZip | DecompressionMethods.Deflate;

            using (HttpWebResponse response = (HttpWebResponse)await request.GetResponseAsync())
            using (Stream stream = response.GetResponseStream())
            using (StreamReader reader = new StreamReader(stream))
            {
                var result = await reader.ReadToEndAsync();
                System.Console.WriteLine(result);
                return result;//todo:remove cw
            }
        }
    }
}
