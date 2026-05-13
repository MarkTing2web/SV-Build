const sharp = require('sharp');
const fs = require('fs');

async function processImage(inputPath, outputPath, width, height, quality) {
  try {
    await sharp(inputPath)
      .resize(width, height, { fit: 'cover' })
      .webp({ quality: quality })
      .toFile(outputPath);
    console.log('Processed', outputPath);
  } catch (err) {
    console.error('Error processing', inputPath, err);
  }
}

async function run() {
  // Image 3
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/wifi_generations_router_1778668591632.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/wifi-generations-router.webp', 800, 600, 85);
  // Image 4
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/ethernet_port_smart_tv_1778668735021.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/ethernet-port-smart-tv.webp', 800, 600, 85);
}

run();
