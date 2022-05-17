import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SecretComponent } from "./secret/secret.component";
import { MainComponent } from "./main/main.component";
import { environment } from "../environments/environment";

const routes: Routes = [
  {
    path: `secret/page/is/here`,
    component: SecretComponent
  },
  {
    path: `**`,
    component: MainComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
