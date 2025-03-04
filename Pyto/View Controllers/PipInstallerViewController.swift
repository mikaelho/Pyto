//
//  PipInstallerViewController.swift
//  Pyto
//
//  Created by Adrian Labbé on 3/20/19.
//  Copyright © 2019 Adrian Labbé. All rights reserved.
//

import UIKit

/// A View controller for running `pip` commands.
@objc class PipInstallerViewController: EditorSplitViewController {
    
    /// Closes this View controller.
    @objc func closeViewController() {
        
        let window = view.window
        
        return dismiss(animated: true, completion: {
            ((window?.rootViewController?.presentedViewController as? UINavigationController)?.visibleViewController as? PipViewController)?.webView.reload()
        })
    }
    
    private var command = ""
    
    /// Initializes for running given `pip` command.
    ///
    /// - Parameters:
    ///     - command: The command to run. Without the program name. For example, `install bottle` for running `pip install bottle`.
    init(command: String) {
        super.init(nibName: nil, bundle: nil)
        self.command = command
    }
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
    }
    
    /// The last visible instance.
    static var shared: PipInstallerViewController?
    
    // MARK: - Editor split view controller
    
    #if !targetEnvironment(macCatalyst)
    override var keyCommands: [UIKeyCommand]? {
        return [UIKeyCommand(input: "C", modifierFlags: .control, action: #selector(interrupt), discoverabilityTitle: Localizable.interrupt)]
    }
    #endif
    
    override func loadView() {
        super.loadView()
        
        ratio = 0
        
        if let repl = Bundle.main.url(forResource: "installer", withExtension: "py") {
            editor = EditorViewController(document: PyDocument(fileURL: repl))
            editor.args = command
        }
        console = ConsoleViewController()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        arrangement = .horizontal
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        navigationItem.leftBarButtonItems = []
        navigationItem.rightBarButtonItems = []
        navigationController?.isToolbarHidden = true        
        PipInstallerViewController.shared = self
        
        navigationItem.leftBarButtonItems = [UIBarButtonItem(barButtonSystemItem: .done, target: self, action: #selector(closeViewController))]
        navigationItem.leftBarButtonItem?.isEnabled = false
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        if let path = editor.document?.fileURL.path, Python.shared.isScriptRunning(path) {
            editor.stop()
            DispatchQueue.main.asyncAfter(deadline: .now()+2) {
                self.editor.run()
            }
        } else {
            DispatchQueue.main.asyncAfter(deadline: .now()+1) {
                self.editor.run()
            }
        }
    }
    
    override func willTransition(to newCollection: UITraitCollection, with coordinator: UIViewControllerTransitionCoordinator) {}
}

