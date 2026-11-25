import AppKit

let canvas = NSSize(width: 1200, height: 1000)
let ink = NSColor(srgbRed: 0.09, green: 0.13, blue: 0.11, alpha: 1)
let green = NSColor(srgbRed: 0.07, green: 0.34, blue: 0.25, alpha: 1)
let paper = NSColor(srgbRed: 0.97, green: 0.96, blue: 0.92, alpha: 1)
let paleGreen = NSColor(srgbRed: 0.89, green: 0.93, blue: 0.87, alpha: 1)

func render(_ language: String) throws {
    let chinese = language == "zh"
    let image = NSImage(size: canvas, flipped: true) { bounds in
        paper.setFill()
        bounds.fill()

        func label(
            _ text: String,
            x: CGFloat = 76,
            y: CGFloat,
            size: CGFloat,
            weight: NSFont.Weight = .regular,
            color: NSColor = ink
        ) {
            (text as NSString).draw(
                at: NSPoint(x: x, y: y),
                withAttributes: [
                    .font: NSFont.systemFont(ofSize: size, weight: weight),
                    .foregroundColor: color,
                ]
            )
        }

        func rule(at y: CGFloat) {
            green.setFill()
            NSRect(x: 76, y: y, width: 1048, height: 3).fill()
        }

        label(
            chinese ? "生成式软件工程（GSE）" : "Generative Software Engineering (GSE)",
            y: 58,
            size: 30,
            weight: .semibold,
            color: green
        )
        rule(at: 122)

        if chinese {
            label("测试过了，", y: 155, size: 64, weight: .bold)
            label("不代表你用的是新版", y: 235, size: 64, weight: .bold)
        } else {
            label("Tests passed.", y: 155, size: 64, weight: .bold)
            label("That isn't proof the app is new.", y: 235, size: 55, weight: .bold)
        }

        paleGreen.setFill()
        NSBezierPath(
            roundedRect: NSRect(x: 76, y: 370, width: 1048, height: 390),
            xRadius: 22,
            yRadius: 22
        ).fill()

        label(
            chinese ? "AI 说“完成”时，分开核对三件事" : "When AI says “done,” check three claims separately",
            x: 111,
            y: 400,
            size: 34,
            weight: .semibold
        )

        let checks = chinese
            ? [
                "代码已经进入项目主线",
                "装上的应用来自这次构建",
                "真实操作路径确实可用",
            ]
            : [
                "The code is in the project's main branch",
                "The installed app comes from that build",
                "The real user path actually works",
            ]

        for (index, check) in checks.enumerated() {
            let y = CGFloat(482 + 78 * index)
            label(String(index + 1), x: 116, y: y, size: 32, weight: .bold, color: green)
            label(check, x: 176, y: y, size: 35, weight: .semibold)
        }

        label(
            chinese
                ? "最近一次检查：29 份安装记录中，5 份来自未合入主线的源码"
                : "Recent audit: 5 of 29 app installs used source outside main",
            y: 815,
            size: chinese ? 29 : 31,
            weight: .medium
        )
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
