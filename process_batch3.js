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
  // Image 9
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/cat7_cable_retry2_1778671168511.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/cat7-cable.webp', 960, 540, 85);
  // Image 10
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/cat3_vs_cat6_wall_plate_retry2_1778671256168.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/cat3-vs-cat6-wall-plate.webp', 800, 600, 85);
  // Image 11
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/network_switch_poe_rack_retry2_1778671388605.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/network-switch-poe-rack.webp', 800, 600, 85);
}

run();
