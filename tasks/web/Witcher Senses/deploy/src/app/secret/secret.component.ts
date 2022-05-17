import { Component, OnInit } from '@angular/core';
import { SecretService } from "./secret.service";

@Component({
  selector: 'app-secret',
  templateUrl: './secret.component.html',
  styleUrls: ['./secret.component.scss']
})
export class SecretComponent implements OnInit {

  flag!: string;

  constructor(private secretService: SecretService) { }

  ngOnInit(): void {
    this.flag = this.secretService.getFlag();
  }

}
