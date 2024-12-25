// ==UserScript==
// @name         题目内容获取器
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  获取题目编辑器内容
// @author       Your name
// @match        https://www.marscode.cn/practice/*?problem_id=*
// @grant        GM_setClipboard
// ==/UserScript==

(function () {
  "use strict";

  function getAnswerString() {
    const editor = document
      .querySelector("icube-markdown")
      .shadowRoot.querySelector(".icube-markdown");
    if (editor) {
      return editor.textContent;
    } else {
      return "未找到编辑器";
    }
  }

  // 创建复制按钮
  function createButton(text, contentGetter, setStyle) {
    const button = document.createElement("button");
    button.innerHTML = text;
    button.style.position = "fixed";
    button.style.top = "10px";
    button.style.right = "10px";
    button.style.zIndex = "9999";
    button.style.padding = "8px 16px";
    button.style.backgroundColor = "#4CAF50";
    button.style.color = "white";
    button.style.border = "none";
    button.style.borderRadius = "4px";
    button.style.cursor = "pointer";
    setStyle(button.style);

    button.addEventListener("click", async function () {
      const content = contentGetter();
      await GM.setClipboard(content, "text");
      button.innerHTML = "已复制！";
      setTimeout(() => {
        button.innerHTML = text;
      }, 2000);
    });

    return button;
  }

  function createAnswer() {
    return createButton("复制答案", getAnswerString, (style) => {});
  }

  function ojOutput() {
    return createButton(
      "复制错误",
      () => {
        const output = document.querySelector(".oj-output").innerText;
        return output;
      },
      (style) => {
        style.top = "70px";
      }
    );
  }

  document.body.appendChild(createAnswer());
  document.body.appendChild(ojOutput());
})();
