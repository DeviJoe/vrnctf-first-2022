import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ctf-spell-2';
  isMindReadSign = null;

  async isMindRead() {
    // todo check if any spell vulnerability here
    // @ts-ignore
    this.isMindReadSign = (await import(`src/app/jsfuck/is-mind-read.js`)).default();
    setTimeout(() => {
      this.isMindReadSign = null;
    }, 100);
  }

  async readMind() {
    // @ts-ignore
    return (await import(`src/app/jsfuck/read-mind.js`)).default();
  }
}
