import { Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { environment } from "../../environments/environment";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit, OnDestroy {
  private letterIndex = 0;
  letter!: string;

  private interval!: number;

  constructor() { }

  ngOnInit(): void {
    this.interval = setInterval(() => {
      this.letterIndex = (this.letterIndex + 1) % environment.path.length;
      this.letter = environment.path[this.letterIndex];
    }, 15);
  }

  ngOnDestroy(): void {
    clearInterval(this.interval);
  }


}
