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
  // Image 5
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/mesh_wifi_placement_home_1778669170880.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/mesh-wifi-placement-home.webp', 800, 600, 85);
  // Image 6
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/cat5e_cable_1778669374155.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/cat5e-cable.webp', 960, 540, 85);
}

run();
