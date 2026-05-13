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
  // Image 7
  await processImage('C:/Users/Ler Wee Meng/.gemini/antigravity/brain/42bf86c2-7ba9-4d93-98bf-cd0ddfcf5e28/cat6_cable_cross_section_1778669804838.png', 'd:/Ler Wee Meng/Project-Web/SV-Build/images/resources/guides/network/cat6-cable-cross-section.webp', 960, 540, 85);
}

run();
