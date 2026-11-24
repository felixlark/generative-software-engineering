import AppKit

let canvas = NSSize(width: 1200, height: 1000)
let ink = NSColor(srgbRed: 0.09, green: 0.13, blue: 0.11, alpha: 1)
let green = NSColor(srgbRed: 0.09, green: 0.34, blue: 0.26, alpha: 1)
let paper = NSColor(srgbRed: 0.97, green: 0.96, blue: 0.92, alpha: 1)
let paleGreen = NSColor(srgbRed: 0.89, green: 0.93, blue: 0.87, alpha: 1)

func render(_ language: String) throws {
    let chinese = language == "zh"
    let image = NSImage(size: canvas, flipped: true) { bounds in
        paper.setFill()
        bounds.fill()
        func label(_ text: String, x: CGFloat = 76, y: CGFloat, size: CGFloat,
                   weight: NSFont.Weight = .regular, color: NSColor = ink) {
            (text as NSString).draw(at: NSPoint(x: x, y: y), withAttributes: [
                .font: NSFont.systemFont(ofSize: size, weight: weight),
                .foregroundColor: color,
            ])
        }
        func rule(at y: CGFloat) {
            green.setFill()
            NSRect(x: 76, y: y, width: 1048, height: 3).fill()
        }
        label(chinese ? "生成式软件工程（GSE）" : "Generative Software Engineering (GSE)",
              y: 58, size: 30, weight: .semibold, color: green)
        rule(at: 122)
        label(chinese ? "Chrome 扩展更新了？" : "Updated a Chrome extension?",
              y: 156, size: 62, weight: .bold)
        label(chinese ? "先看它从哪加载" : "Check where it loads from",
              y: 235, size: 70, weight: .bold)
        label(chinese ? "两个目录里的开发版扩展，可能显示同一个版本号。" :
              "Two folders can hold copies with the same version number.",
              y: 348, size: 32)
        let steps = chinese
            ? ["打开 chrome://extensions", "进扩展详情，核对「加载来源」", "从正确目录加载，再刷新页面试一次"]
            : ["Open chrome://extensions", "Check “Loaded from” in the extension details", "Load from the right folder, then test the page"]
        paleGreen.setFill()
        NSBezierPath(roundedRect: NSRect(x: 76, y: 430, width: 1048, height: 326),
                     xRadius: 22, yRadius: 22).fill()
        for (index, step) in steps.enumerated() {
            let y = CGFloat(460 + 92 * index)
            label(String(index + 1), x: 111, y: y, size: 35, weight: .bold, color: green)
            label(step, x: 174, y: y, size: 38, weight: .semibold)
        }
        label(chinese ? "GSE 新增了扩展换目录后的核对方法。" :
              "GSE added a workflow for checking extension folder changes.",
              y: 805, size: 32)
        rule(at: 886)
        label("@felixlark", y: 915, size: 30, weight: .semibold, color: green)
        return true
    }
    guard let data = image.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: data),
          let png = bitmap.representation(using: .png, properties: [:]) else {
        throw CocoaError(.fileWriteUnknown)
    }
    try png.write(to: URL(fileURLWithPath: "poster-\(language).png"))
}

try render("zh")
try render("en")
