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
  // Image 12
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/ip_address_static_diagram_batch3_1778671558428.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/ip-address-static-diagram.webp', 800, 600, 85);
}

run();
